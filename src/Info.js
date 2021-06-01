import React, {useState} from 'react'
import { useParams } from 'react-router-dom'

export default function Info({ match }) {



  return (
    <h2>
      Info
      {match.params.name}
    </h2>
  )
}