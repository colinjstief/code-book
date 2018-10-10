import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Header, Icon } from 'semantic-ui-react';

const NotFound = () => (
  <div className="page-404">
    <Container>
      <Header as="h2" icon>
        <Icon name="question circle outline" />
        Can't find that page!
        <Header.Subheader>
          <Link className="link-blue" to="/">Return home!</Link> or try something else...
        </Header.Subheader>
      </Header>
    </Container>
  </div>
);

export default NotFound;