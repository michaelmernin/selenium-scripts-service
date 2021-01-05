
# Selenium Scripts API
Restful service provides the ability to perform selenium actions through http post requests.  

## Supported Methods
POST/ runScript  
All requests will be made to this endpoint

## Examples
Examples show the minimum/required values for each request.
All scripts must be added to the requests [ ] (see "Making Requests" below)
> Please see the 'Parameters' section (below) for specs on all parameters offered
### Example Script
```json
{	
	"script_action": "example_script",
	"attribute_1": "1",
	"attribute_2": "1",
}
```
# Making Requests -- Extended Scenarios
> All requests must be placed within "requests": []
#### Calling multiple scripts in a single request
```json
{

	"requests": [
	{	
	"script_action": "example_script",
	"attribute_1": "1",
	"attribute_2": "1",
    },
    {	
        "script_action": "example_script",
        "attribute_1": "1",
        "attribute_2": "1",
    }
  ]
}
```

## Parameters (Work in Progress)
#### Example Script
| param | options/explanation | Required | example values |
| ------ | ------ | ------ | ----- |
| attribute_1 | NONE | YES | example |
| attribute_2 | NONE | YES | example |
