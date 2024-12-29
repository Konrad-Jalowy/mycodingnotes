import { createContext, useContext, useReducer } from 'react';

const initialState = {
    shuffle: false,
    title: null,
    firstIdx: 0,
    lastIdx: null,
    take: null,
    datesFirst: true,
    dates: [],
    loopMode: 'fileNotSent'
};

function appContextReducer(state, action){
    switch (action.type) {
        case 'toggleShuffle': {
          return {
            ...state, 
            shuffle: !state.shuffle
          };
        }
        case 'toggleDatesFirst': {
            return {
              ...state, 
              datesFirst: !state.datesFirst
            };
          }
          case 'setTitle': {
            return {
              ...state, 
              title: action.payload
            };
          }
          case 'setDates': {
            return {
              ...state, 
              dates: [...action.payload]
            };
          }
          case 'setTake': {
            return {
              ...state, 
              take: action.payload
            };
          }
          case 'setLastIdx': {
            return {
              ...state, 
              lastIdx: action.payload
            };
          }
          case 'setLoopMode': {
            return {
              ...state, 
              loopMode: action.payload
            };
          }
          case 'prepare': {
            return {
              ...state, 
              loopMode: 'started',
              title: action.payload.title,
              take: action.payload.take,
              datesFirst: action.payload.datesFirst,
              shuffle: action.payload.shuffle,
              dates: action.payload.dates
            };
          }
          case 'reset': {
            return {   
            shuffle: false,
            title: null,
            firstIdx: 0,
            lastIdx: null,
            take: null,
            datesFirst: true,
            dates: [],
            loopMode: 'fileNotSent'
            };
          }
        
        
        default: {
          throw Error('Unknown action: ' + action.type);
        }
      }
    }
    

    const AppContext = createContext(null);
    
    const AppDispatchContext = createContext(null);
    
    export function AppProvider({ children }) {
        const [state, dispatch] = useReducer(appContextReducer, initialState);
      
        return (
          <AppContext.Provider value={state}>
            <AppDispatchContext.Provider value={dispatch}>
              {children}
            </AppDispatchContext.Provider>
          </AppContext.Provider>
        );
      }
    
      export function useApp() {
        return useContext(AppContext);
      }
      
      export function useAppDispatch() {
        return useContext(AppDispatchContext);
      }
    
      export function useAppWithDispatch(){
        return [useContext(AppContext), useContext(AppDispatchContext) ];
      }