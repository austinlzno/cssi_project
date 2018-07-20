// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

let customer_name;
let balance;

function openAccount(name, startingBalance=0, logged_in){
  balance = startingBalance;
  customer_name = name;
  console.log(customer_name);
  return  `${name} has opened a new account with a balance of $${startingBalance}`;
}

function deposit(value)
{
balance = value + balance;
  console.log(balance);
  return `${customer_name} has deposited ${value}. ${customer_name}'s total balance is ${balance}`;

}


function withdraw(value){
  balance = balance - value;
  console.log(balance);
return `${customer_name} has withdrawn ${value}. ${customer_name} has ${balance} remaining`;

}

// Write your script below
