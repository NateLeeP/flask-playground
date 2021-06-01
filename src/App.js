import React, { useState } from 'react'
import HelloWorld from './HelloWorld.js'
import About from './About'
import Info from './Info'

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useParams
} from "react-router-dom";


function App ({}) {


  return (
    <Router>
      <div>
        <Link to="/greetings/home">Home</Link>
        <Link to="/greetings/about">About</Link>
      </div>
      <Switch>
        <Route path='/greetings/about'>
          <About />
        </Route>
        <Route path='/greetings/info/:name' component={Info} />
        <Route path='/greetings/home'>
          <HelloWorld />
        </Route>
      </Switch>
    </Router>
  )
}

ReactDOM.render(<App />, document.getElementById('app'))