# ValidateHostRequestType

The parameters of *OvfManager.ValidateHost*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ovf_descriptor** | **str** | The OVF descriptor to examine.  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vhp** | [**OvfValidateHostParams**](OvfValidateHostParams.md) |  | 

## Example

```python
from vmware_vi.models.validate_host_request_type import ValidateHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateHostRequestType from a JSON string
validate_host_request_type_instance = ValidateHostRequestType.from_json(json)
# print the JSON string representation of the object
print ValidateHostRequestType.to_json()

# convert the object into a dict
validate_host_request_type_dict = validate_host_request_type_instance.to_dict()
# create an instance of ValidateHostRequestType from a dict
validate_host_request_type_form_dict = validate_host_request_type.from_dict(validate_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


