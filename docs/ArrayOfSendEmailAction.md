# ArrayOfSendEmailAction

A boxed array of *SendEmailAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SendEmailAction]**](SendEmailAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_send_email_action import ArrayOfSendEmailAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSendEmailAction from a JSON string
array_of_send_email_action_instance = ArrayOfSendEmailAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfSendEmailAction.to_json()

# convert the object into a dict
array_of_send_email_action_dict = array_of_send_email_action_instance.to_dict()
# create an instance of ArrayOfSendEmailAction from a dict
array_of_send_email_action_form_dict = array_of_send_email_action.from_dict(array_of_send_email_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


