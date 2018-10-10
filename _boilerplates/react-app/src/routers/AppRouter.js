import React from 'react';

// Router
import { Router, Route, Switch } from 'react-router-dom';
import createHistory from 'history/createBrowserHistory';
export const history = createHistory();

// Components
import AppContainer from '../components/AppContainer/AppContainer';
import NotFoundPage from '../components/NotFound/NotFound';

const AppRouter = () => (
  <Router history={history}>
    <div>
      <Switch>
        <Route path="/" exact component={AppContainer} />
        <Route component={NotFoundPage} />
      </Switch>
    </div>
  </Router>
);

export default AppRouter;