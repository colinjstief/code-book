const records = [
  {
    lat: 38.23,
    lon: -57.65,
    name: 'Here',
    cost: 1239
  },
  {
    lat: 40.50,
    lon: -60.31,
    name: 'There',
    cost: 2392
  },
  {
    lat: 29.93,
    lon: -58.39,
    name: 'Unknown',
    cost: 3092
  }
];

////////////////
// Filter
const text = 'Here';
const newRecords = records.filter((record) => {
  return record.name.toLowerCase().includes(text.toLowerCase());
});

////////////////
// Map
const newRecords = records.map((record, index) => {
  return `<li data-lat="${record.lat}" data-lon="${record.lon}">${record.name}</li>`
});

////////////////
// Concat


////////////////
// Reduce
const addCallback = (sum, value) => sum + value;
const total = records.map(record => record.cost).reduce(addCallback);

////////////////
// Sort (objects)

const records = [{ createdAt: 2000 }, { createdAt: 1500 }, { createdAt: 5000 }, { createdAt: 300 }];
sortedRecords = records.sort((a, b) => {
  return a.createdAt < b.createdAt ? 1 : -1;
});

// Alt -- iplicit return
sortedRecords = records.sort((a, b) => a.createdAt < b.createdAt ? 1 : -1);