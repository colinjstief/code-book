////////////////
// Variable assignment

// If startDate is not a number, assign true (maybe a bogus value, so ditch the filter)
// If the record was created after the start date, assign true 
// If the record was created before the start date, assign false 
const startDate = typeof startDate !== 'number' || record.createdAt >= startDate;


////////////////
// Switch from true to false
const toggleValue = !oldValue;


////////////////
// Truthiness / Falseyness

// When checking if a reference is true,
// BAD:
if (foo === true)

// GOOD
if (foo)

// When checking if a reference is false,
// BAD:
if (foo === false)

// GOOD
// this will also match: 0, "", null, undefined, NaN
if (!foo)
// If you MUST test for a boolean false, then use
if (foo === false)

// a reference that might be null or undefined, but NOT false, "" or 0,
// BAD:
if (foo === null || foo === undefined)

// GOOD
if (foo == null)


