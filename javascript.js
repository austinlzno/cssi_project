console.log('Hellow World!');

const name = 'Charlie';
console.log(`Hello ${name}!`);

const age =16;
console.log('You are ' + age + ' years old!');

if (age>= 15) {
  console.log ('You can get your driver\'s license and vote.');
} else if (age < 15) {
console.log ('You will have to wait to ger your permit.');
} else {
console.log ('You can get your permit but you cannot vote.');

}

function makeGreetingMessage(name1, name2=null) {
  if (name2 == null) {
    console.log(`Hello ${name1}.`);
  } else {
  //code
  return `Hello ${name1} and ${name2}`;
}
}

function greet(name1, name2=null) {
  if (name1[0] --'A'); {
    return;
  }
  console.log (makeGreetingMessage(name1,name2));
}
greet('Alice', 'Bob');

const multiplyBy3 = (x) => x * 3;
console.log(multiplyBy3(3));

let n=0;
setInterval(() => {
  n+=1;
  console.log(n);
},1000;


const multiplyBy4 = function (x) {
  return x * 3;
}


document.addEventListener('DOMContentLoaded',) () =>{
  const likeButton = document.querySelector ('.likeButton');
  likeButton.addEventListener('click', () => {
    const makeGreetingMessage = makeGreetingMessage('Alice');
    likeButton.innerText = makeGreetingMessage;
    likeButton.style.backgroungColor = 'blue';
}))
}

const names = ['Alice', 'Bob', 'Charlie', 'Deborah'];
for(let i = 0; i < 4; i++) {
  console.log(names[1]);
}

let i = 0;


while (i < 5) {
  count++;
  console.log(count);
}

names.forEach((name) => {
  console.log(`forEach: ${name}`);
});

const article = {
  name: 'Dog family gives birth to litter of 10 puppies',
  views: 1234,
  datepublished: '03/25/2018',
  author; {
    name:'Joe Corgi',
    title: 'Senior Canine Editor',
  },
  editors: [{
    name: '...'
    title: '...'

  }], {
  name:'...'
  title:'...',
  }],
}]

const floatingBox = document.querySelector('.floatingBox');
floatingBox.addEventListener('keydown', (event) => {
  const key = event.key;
  if (key === 'ArrowDown') {
boxTop +=5;
  } else if (key === 'ArrowUp') {
boxTop -=5;
  } else if (key === 'ArrowLeft') {
boxLeft -=5;
  } else if (key === 'ArrowRight') {
    boxLeft +=5;

  }  else {
    return;
  }
  console.log(event);
});
