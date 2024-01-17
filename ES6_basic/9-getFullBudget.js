import getBudgetObject from './7-getBudgetObject.js'

// task9
export default function getFullBudgetObject (income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita)
  const fullBudget = {
    ...budget,
    getIncomeInDollars (incomeAmount) {
      return `$${incomeAmount}`
    },
    getIncomeInEuros (incomeAmount) {
      return `${incomeAmount} euros`
    }
  }

  return fullBudget
}
