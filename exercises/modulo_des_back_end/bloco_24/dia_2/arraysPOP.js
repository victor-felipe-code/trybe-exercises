// =================== << TRYBE >> ==========================
// =========== << https://app.betrybe.com/ >> ===============


// Removendo o primeiro item de um array
db.supplies.updateOne({ _id: 1 }, { $pop: { items: -1 } });


//Removendo o último item de um array
db.supplies.updateOne({ _id: 1 }, { $pop: { items: 1 } });