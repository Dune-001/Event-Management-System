import { useEffect, useState } from "react";
import { EventService } from '../services/api';

/**
 * EventList Component - Displays a list of all events
 * This component shows how to fetch data from the api and displays it
 */
const EventList = ({ onEventSelect }) => {
    // state to store events data
    const [events, setEvents] = useState([]);
    // state to track loading status
    const [loading, setLoading] = useState(true);
    // state to track errors
    const [error, setError] = useState(null);

    /**
     * useEffect hook - runs when component mounts
     * similar to componentDidMount in class components
     */
    useEffect(() => {
        loadEvents();
    }, []); // empty dependency array means run only once

    /**
     * Function to load events from API
     */
    const loadEvents = async () => {
        try {
            setLoading(true);
            const eventsData = await EventService.getEvents();
            setEvents(eventsData);
            setError(null);
        } catch (err) {
            setError('Failed to load events. Please try again.');
            console.error('Error loading events:', err);
        } finally {
            setLoading(false);
        }
    };

    // format data to readable string
    const formatDate = (dateString) => {
        return new Date(dateString).toLocaleDateString('en-US', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    };
    if (loading) {
        return (
            <div className="flex justify-center items-center py-8">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
                <p>{error}</p>
                <button
                    onClick={loadEvents}
                    className="mt-2 bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-3 rounded text-sm"
                >
                    Retry
                </button>
            </div>
        );
    }
}