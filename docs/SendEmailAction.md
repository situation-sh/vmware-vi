# SendEmailAction

This data object type defines an email that is triggered by an alarm.  You can use any elements of the *ActionParameter* enumerated list as part of your strings to provide information available at runtime. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_list** | **str** | A comma-separated list of addresses to which the email notification is sent.  | 
**cc_list** | **str** | A comma-separated list of addresses that are cc&#39;ed on the email notification.  | 
**subject** | **str** | Subject of the email notification.  | 
**body** | **str** | Content of the email notification.  | 

## Example

```python
from vmware_vi.models.send_email_action import SendEmailAction

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailAction from a JSON string
send_email_action_instance = SendEmailAction.from_json(json)
# print the JSON string representation of the object
print SendEmailAction.to_json()

# convert the object into a dict
send_email_action_dict = send_email_action_instance.to_dict()
# create an instance of SendEmailAction from a dict
send_email_action_form_dict = send_email_action.from_dict(send_email_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


