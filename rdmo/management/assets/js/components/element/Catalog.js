import React, { Component } from 'react'
import PropTypes from 'prop-types'
import isUndefined from 'lodash/isUndefined'

import { filterElements } from '../../utils/filter'

import Section from './Section'
import { EditLink, AvailableLink, LockedLink, NestedLink, ExportLink } from '../common/ElementLinks'

const Catalog = ({ config, catalog, fetchElement, storeElement, list=true }) => {

  const verboseName = gettext('catalog')

  const fetchEdit = () => fetchElement('catalogs', catalog.id)
  const fetchNested = () => fetchElement('catalogs', catalog.id, 'nested')
  const toggleAvailable = () => storeElement('catalogs', {...catalog, available: !catalog.available })
  const toggleLocked = () => storeElement('catalogs', {...catalog, locked: !catalog.locked })

  const elementNode = (
    <div className="element">
      <div className="element-options">
        <EditLink element={catalog} verboseName={verboseName} onClick={fetchEdit} />
        <AvailableLink element={catalog} verboseName={verboseName} onClick={toggleAvailable} />
        <LockedLink element={catalog} verboseName={verboseName} onClick={toggleLocked} />
        <NestedLink element={catalog} verboseName={verboseName} onClick={fetchNested} />
        <ExportLink element={catalog} verboseName={verboseName} />
      </div>
      <div>
        <p>
          <strong>{gettext('Catalog')}{': '}</strong> {catalog.title}
        </p>
        <p>
          <code className="code-questions">{catalog.uri}</code>
        </p>
      </div>
    </div>
  )

  if (list) {
    return (
      <li className="list-group-item">
        { elementNode }
      </li>
    )
  } else {
    return elementNode
  }
}

Catalog.propTypes = {
  config: PropTypes.object.isRequired,
  catalog: PropTypes.object.isRequired,
  fetchElement: PropTypes.func.isRequired,
  storeElement: PropTypes.func.isRequired,
  list: PropTypes.bool
}

export default Catalog
