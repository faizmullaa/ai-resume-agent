import {useState} from 'react'
import axios from 'axios'

export default function UploadForm(){
  const [file,setFile]=useState(null)
  const [res,setRes]=useState(null)

  const up=async(e)=>{
    e.preventDefault()
    const fd=new FormData()
    fd.append('file',file)
    const r=await axios.post(process.env.NEXT_PUBLIC_BACKEND_URL+'/api/upload',fd)
    setRes(r.data)
  }

  return <div>
    <form onSubmit={up}>
      <input type='file' onChange={e=>setFile(e.target.files[0])}/>
      <button>Upload</button>
    </form>
    {res && <pre>{JSON.stringify(res,null,2)}</pre>}
  </div>
}
