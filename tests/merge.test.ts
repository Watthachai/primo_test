import { merge } from '../src/merge';

describe('merge function', () => {
    it ('should merger all 3 collections correctly', () => {
        const collection_1 = [1, 2, 4, 9];
        const collection_2 = [8, 7, 5, 3];
        const collection_3 = [6, 10, 11];

        const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
        expect(merge(collection_1, collection_2, collection_3)).toEqual(expected);
    });

    it ('should handle all empty collections', () => {
        const collection_1: number[] = [];
        const collection_2: number[] = [];
        const collection_3: number[] = [];

        const expected: number[] = [];
        expect(merge(collection_1, collection_2, collection_3)).toEqual(expected);
    })

    it ('should handle some empty arrays', () => {
        const collection_1 = [1, 2, 4, 9];
        const collection_2: number[] = [];
        const collection_3 = [6, 10, 11];

        const expected = [1, 2, 4, 6, 9, 10, 11];
        expect(merge(collection_1, collection_2, collection_3)).toEqual(expected);
    })

    it('should handle arrays with duplicate numbers', () => {
        const collection_1 = [1, 3, 3, 5];
        const collection_2 = [6, 4, 4, 2]; 
        const collection_3 = [1, 7, 7];
        const expected = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7, 7];
        expect(merge(collection_1, collection_2, collection_3)).toEqual(expected);
    });
    
    it('should handle arrays of different lengths', () => {
        const collection_1 = [1];
        const collection_2 = [10, 9, 8, 7, 6, 5]; 
        const collection_3 = [11, 12, 13];
        const expected = [1, 5, 6, 7, 8, 9, 10, 11, 12, 13];
        expect(merge(collection_1, collection_2, collection_3)).toEqual(expected);
    });
    
    it('should handle negative numbers', () => {
        const collection_1 = [-5, -1, 0];
        const collection_2 = [2, -3]; // Descending -> [-3, 2]
        const collection_3 = [-4, 1];
        const expected = [-5, -4, -3, -1, 0, 1, 2];
        expect(merge(collection_1, collection_2, collection_3)).toEqual(expected);
    });
})