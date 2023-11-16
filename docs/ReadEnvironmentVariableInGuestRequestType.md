# ReadEnvironmentVariableInGuestRequestType

The parameters of *GuestProcessManager.ReadEnvironmentVariableInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**names** | **List[str]** | The names of the variables to be read. If not set, then all the environment variables are returned.  | [optional] 

## Example

```python
from vmware_vi.models.read_environment_variable_in_guest_request_type import ReadEnvironmentVariableInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReadEnvironmentVariableInGuestRequestType from a JSON string
read_environment_variable_in_guest_request_type_instance = ReadEnvironmentVariableInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ReadEnvironmentVariableInGuestRequestType.to_json()

# convert the object into a dict
read_environment_variable_in_guest_request_type_dict = read_environment_variable_in_guest_request_type_instance.to_dict()
# create an instance of ReadEnvironmentVariableInGuestRequestType from a dict
read_environment_variable_in_guest_request_type_form_dict = read_environment_variable_in_guest_request_type.from_dict(read_environment_variable_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


