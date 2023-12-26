# TASK MANAGER (WITH PYTHON DJANGO + POSRGRESQL)

## Drive  Video Link https://drive.google.com/file/d/1ofmU6Yekvphmjg_PENAdWMv8XMASLX40/view?usp=sharing

## Video


## Images

### HomePage
![Homepage](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/a5a619f0-eeb0-405e-b6f8-9b514b3737d5)

### Login Page
![Login_Page](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/9496d69e-e190-4498-92b6-08cc9214954f)

### Register Page
![Register_page](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/a55ac4e5-2e41-47b3-a999-7dd146725b41)

### View Task
![ViewPAge](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/b9158969-eb45-402f-b215-fe22c1f5783a)

### Update Task
![UpdateTask](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/decb3cfe-b074-4d27-a5da-8c098f76e365)

### Delete Task
![Deletetask](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/0a2ce139-4752-4005-83b4-f0945b8d59e6)

### CreateTAskPAge
![CreateTaskPage](https://github.com/Ronnie-Ahmed/Task_manager/assets/68500792/2a23affb-1761-427c-9043-a567691801aa)


## How to install

> 1. Clone the repository
>    > `git clone -b dev.0.0.1 https://github.com/Ronnie-Ahmed/Task_manager.git`
> 2. Create a virtual environment
>    > `virtualenv env`
> 3. Activate the virtual environment
>    > `.env\Scripts\activate` (Windows)
>    > `source env/bin/activate` (Linux)
> 4. Install the requirements
>    > `pip install -r requirements.txt`
> 5. modify `.env.example` to `.env` and add your database credentials
>
> ##
>
> > > > 6. If I haven't uploaded a folder named `media` then create a folder named `media` in the root directory
>
> ##
>
> 7. Run the migrations
>    > `python manage.py migrate`
> 8. Run the server
>    > `python manage.py runserver` 9. Open the browser and go to `http://127.0.0.1:8000/` 10. Enjoy

## How to use

> 1. Create a new user
> 2. Login with the new user
> 3. Create a new task
> 4. View the task
> 5. Edit the task
> 6. Delete the task
> 7. Logout
> 8. Enjoy

# My Introduction (Use Remix IDE to run the code)

```Solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Introduction{
    function decodeHash(bytes memory hash) public pure returns(string memory Name, string memory Github,string memory Email,string memory Website)
    {
        (Name,Github,Email,Website)=abi.decode(hash, (string ,string,string,string));
    }
}
```

> > hash=0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001200000000000000000000000000000000000000000000000000000000000000160000000000000000000000000000000000000000000000000000000000000001352616973756c2049736c616d20526f6e6e696500000000000000000000000000000000000000000000000000000000000000000000000000000000000000002268747470733a2f2f706f7274666f6c696f2d666c326c2e76657263656c2e6170702f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000013726b7372616973756c40676d61696c2e636f6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001f68747470733a2f2f6769746875622e636f6d2f526f6e6e69652d41686d656400
