# UpdateServiceMessageRequestType

The parameters of *SessionManager.UpdateServiceMessage*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message to send. Newline characters may be included.  | 

## Example

```python
from vmware_vi.models.update_service_message_request_type import UpdateServiceMessageRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServiceMessageRequestType from a JSON string
update_service_message_request_type_instance = UpdateServiceMessageRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateServiceMessageRequestType.to_json()

# convert the object into a dict
update_service_message_request_type_dict = update_service_message_request_type_instance.to_dict()
# create an instance of UpdateServiceMessageRequestType from a dict
update_service_message_request_type_form_dict = update_service_message_request_type.from_dict(update_service_message_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


