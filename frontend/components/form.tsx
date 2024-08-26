"use client"
import React, {useState} from 'react';

interface FormData   {
    story: string;
    major: string;
    hobbies: string;
    country: string;
    unique_quality: string;
}

const Form: React.FC = () => {
    
    const [formData, setFormData] = useState<FormData>({

        story: '',
        major: '',
        hobbies: '',
        country: '',
        unique_quality: '',

    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>)  => {
        const {name, value} = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };


    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("ayindhi roo", formData)
        try{
            const response = await fetch('http://127.0.0.1:5000/api/recommend',{
                method: 'POST',
                
                headers: {
                    'content-Type': 'application/json',
                    
                },
                body: JSON.stringify(formData),
            });
            
            if (!response.ok){
                throw new Error('edho dengindhi');
            }
            
            const result = await response.json();
            let recommendation = result.recommendations
            console.log(result.recommendations)

        
        }catch(error){
            console.log('error submitting form',error)
        }
    };

    return (
        <div className="max-w-lg mx-auto p-6 bg-white shadow-md rounded-lg">
            <h2 className="text-2xl font-bold mb-4">Submit Your Information</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-4">
                    <label htmlFor="story" className="block text-sm font-medium text-gray-700">Story</label>
                    <textarea
                        id="story"
                        name="story"
                        value={formData.story}
                        onChange={handleChange}
                        rows={4}
                        className="mt-1 block w-full p-3 border border-gray-300 rounded-md text-black"
                    />
                </div>

                <div className="mb-4">
                    <label htmlFor="major" className="block text-sm font-medium text-gray-700">Major</label>
                    <input
                        type="text"
                        id="major"
                        name="major"
                        value={formData.major}
                        onChange={handleChange}
                        className="mt-1 block w-full p-3 border border-gray-300 rounded-md text-black"
                    />
                </div>

                <div className="mb-4">
                    <label htmlFor="hobbies" className="block text-sm font-medium text-gray-700">Hobbies</label>
                    <input
                        type="text"
                        id="hobbies"
                        name="hobbies"
                        value={formData.hobbies}
                        onChange={handleChange}
                        className="mt-1 block w-full p-3 border border-gray-300 rounded-md text-black"
                    />
                </div>

                <div className="mb-4">
                    <label htmlFor="country" className="block text-sm font-medium text-gray-700">Country</label>
                    <input
                        type="text"
                        id="country"
                        name="country"
                        value={formData.country}
                        onChange={handleChange}
                        className="mt-1 block w-full p-3 border border-gray-300 rounded-md text-black"
                    />
                </div>

                <div className="mb-4">
                    <label htmlFor="unique_quality" className="block text-sm font-medium text-gray-700">Unique Quality</label>
                    <input
                        type="text"
                        id="unique_quality"
                        name="unique_quality"
                        value={formData.unique_quality}
                        onChange={handleChange}
                        className="mt-1 block w-full p-3 border border-gray-300 rounded-md text-black"
                    />
                </div>

                <button
                    type="submit"
                    className="w-full py-3 px-4 bg-blue-500 text-white font-semibold rounded-md shadow-md hover:bg-blue-600"
                >
                    Submit
                </button>
            </form>
        </div>
    )

};

export default Form;
