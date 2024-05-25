import React from 'react';
import {useState, ChangeEvent} from 'react';
import styles from '@/app/ui/panel.module.css'

export default function InputPanel() {
    const [image, setImage] = useState<File|null>(null);
    const [imageURL, setImageURL] = useState<string | null>(null);
    const [summary, setSummary] = useState<string | null>(null);
    const apiURL = "ac52903aeda2d4b7f9c7f759692ec94f-292991886.us-east-1.elb.amazonaws.com";

    const handleImageChange = (event:ChangeEvent<HTMLInputElement>) => {
        const fileDetails = event.target.files ? event.target.files[0] : null;
        if (fileDetails) {
            setImage(fileDetails);
            const reader = new FileReader();
            reader.onload = (event: ProgressEvent<FileReader>) => {
                if (event.target?.result) {setImageURL(event.target.result as string);}
            }
            reader.readAsDataURL(fileDetails);
        }
    }

    const handleImageUpload = async () => {
        if (image == null) {
            return;
        }
        const formData = new FormData();
        formData.append('file', image);

        const response = await fetch(apiURL, {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            // At this point, this response should contain the summary of the report
            // access the summary from the body of the response and use setSummary here.
            // This component will be re-rendered, at which point we can display only the summary
            const data = await response.json()
            setSummary(data.summary);
            alert("Processing successful");
        } else {
            alert("Processing failed");
        }
    }
    // On uploading the image, basically this says that 
    return <div className={styles.master_div}>
    <div className={styles.uploadArea}>
        <div>
            {imageURL ? 
            (<img src = {imageURL} alt = 'Preview'/>)
            : (<div>
                <img src = '/image-icon.png' className={styles.icon}></img>
                <p>Upload your Image here</p>
            </div>)
            }
        </div>
        <div className= {styles.button_row}>
        <input id = 'file-input' style = {{display: 'none'}} type="file" onChange={handleImageChange}/>
        <label htmlFor = 'file-input' className={styles.fileInput}>Choose your file</label>
        <div className={styles.elemSpace}></div>
        <button className={styles.button} onClick={handleImageUpload}>Upload</button>
        </div>

        {summary && (
            <div className= {styles.outputPanel}>
                <h3>Summary</h3>
                <p>{summary}</p>
            </div>
        )}
    </div>
    </div>
}