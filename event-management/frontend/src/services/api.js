import axios from 'axios';

// creating axios instance with base URL for our django API
const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

/**
 * EventService - Handles all api calls related to events
 * Acts as a bridge between our React app and Django API
 */
export const EventService = {
    /**
     * fetches all events from the api
     * @returns {Promise} Promise with events data
     */
    getEvents: async () => {
        try {
            const response = await api.get('/api/events/');
            return response.data;
        } catch (error) {
            console.error('Error fetching events:', error);
            throw error;
        }
    },
    /**
     * Fetch a single event by ID
     * @param {number} id - Event ID
     * @returns {Promise} Promise with event data
     */
    getEvent: async(id) => {
        try {
            const response = await api.get(`/api/events/${id}/`);
            return response.data;
        } catch (error) {
            console.error('Error fetching event:', error);
            throw error;
        }
    },
    /**
     * Register for an event
     * @param {Object} registrationData - Registration data {event, participant_name, participant_email}
     * @returns {Promise} Promise with registration result
     */
    registerForEvent: async (registrationData) => {
        try {
            const response = await api.post('/api/registrations', registrationData);
            return response.data;
        } catch (error) {
            console.error('Error registering for event:', error);
            throw error;
        }
    },
};

export default api;