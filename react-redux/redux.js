/////////////////////
// Simple Reducer ///
/////////////////////
// 1. Reducers are pure function --> only uses what's passed in, nothing from outside
// 2. Never change state or action

import { createStore } from 'redux';
const countReducter = (state = { count: 0 }, action) => {
  switch (action.type) {
    case 'INCREMENT':
       return {
         count: state.count + action.incrementBy
       };
    case 'REST':
       return {
         count: 0
       };
    default:
       return state;
  }
};

const store = createStore(countReducter);

////// Action generator 

const incrementCount = (data = {}) => ({
  type: 'INCREMENT',
  incrementBy: typeof data.incrementBy === 'number' ? data.incrementBy : 1
});

// Alternative --- with argument destructuring
const incrementCount = ({ incrementBy = 1 } = {}) => ({
  type: 'INCREMENT',
  incrementBy
});

store.dispatch(incrementCount({incrementBy: 5 }));


/////////////////////
// Complex Reducer //
/////////////////////
/////////////////////
// 1. Create one reducer for each root property in redux store

import { createStore, combineReducers } from 'redux';
import uuid from 'uuid';


/////////////////
// Actions

const addExpense = (
  { 
    description = '', 
    note = '', 
    amount = 0, 
    createdAt = 0 
  } = {}
) => ({
  type: 'ADD_EXPENSE',
  expense: {
    id: uuid(),
    description,
    note,
    amount,
    createdAt
  }
});

const removeExpense = ({ id } = {}) => ({
  type: 'REMOVE_EXPENSE',
  id
});

const editExpense = ({ id, updates = {} } = {}) => ({
  type: 'EDIT_EXPENSE',
  id,
  updates
});

const setTextFilter = (text = '') => ({
  type: 'SET_TEXT_FILTER',
  text
});

const sortByAmount = () => ({
  type: 'SORT_BY_AMOUNT'
});

const sortByDate = () => ({
  type: 'SORT_BY_DATE'
});

const setStartDate = (startDate) => ({
  type: 'SET_START_DATE',
  startDate
});

const setEndDate = (endDate) => ({
  type: 'SET_END_DATE',
  endDate
});


/////////////////
// Reducers

// Expenses reducer
const expensesReducerDefaultState = [];
const expensesReducer = (state = expensesReducerDefaultState, action) => {
  switch (action.type) {
    case 'ADD_EXPENSE':
      // With an array spread operator
      return [...state, action.expense];
      // Or, with a simple concat
      //return state.concat(action.expense);

    case 'REMOVE_EXPENSE':
      return state.filter(({ id }) => {
        return id !== action.id;
      });

    case 'EDIT_EXPENSE':
      return state.map((expense) => {
        if (expense.id === action.id) {
          return {
            ...expense,
            ...action.updates
          }
        };
        return expense;
      });

    default:
      return state;
  }
};

// Filters reducer
const filtersReducerDefaultState = {
  text: '',
  sortBy: 'date',
  startDate: undefined,
  endDate: undefined
};
const filtersReducer = (state = filtersReducerDefaultState, action) => {
  switch (action.type) {
    case 'SET_TEXT_FILTER':
      return {
        ...state,
        text: action.text
      }

    case 'SORT_BY_AMOUNT':
      return {
        ...state,
        sortBy: 'amount'
      }

    case 'SORT_BY_DATE':
      return {
        ...state,
        sortBy: 'date'
      }

    case 'SET_START_DATE':
      return {
        ...state,
        startDate: action.startDate
      }

    case 'SET_END_DATE':
      return {
        ...state,
        endDate: action.endDate
      }

    default:
      return state;
  }
};


/////////////////
// Store

// Combine the reducers
const store = createStore(
  combineReducers({
    expenses: expensesReducer,
    filter: filtersReducer
  })
);


/////////////////
// Dispatches
const expenseOne = store.dispatch(
  addExpense({
    description: 'Rent',
    amount: 10000
  })
);

const expenseTwo = store.dispatch(
  editExpense({
    id: expenseOne.expense.id,
    update: {
      amount: 500
    }
  })
);

store.dispatch(
  removeExpense({
    id: expenseOne.expense.id
  })
);

store.dispatch(
  setTextFilter('rent')
);

store.dispatch(
  sortByAmount()
);

store.dispatch(
  sortByDate()
);

store.dispatch(
  setStartDate(125)
);

store.dispatch(
  setEndDate(250)
);

/////////////////
// Dummy data

const demoState ={
  expenses: [{
    id: '12312',
    description: 'January Rent',
    note: 'This was the last payment',
    amount: 54500,
    createdAt: 0
  }],
  filters: {
    text: 'rent',
    sortBy: 'date',
    startDate: undefined,
    endDate: undefined
  }
};
