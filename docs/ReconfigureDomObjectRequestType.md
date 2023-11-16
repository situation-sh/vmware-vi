# ReconfigureDomObjectRequestType

The parameters of *HostVsanInternalSystem.ReconfigureDomObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | DOM object UUID.  | 
**policy** | **str** | VSAN expression formatted policy string.  | 

## Example

```python
from vmware_vi.models.reconfigure_dom_object_request_type import ReconfigureDomObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureDomObjectRequestType from a JSON string
reconfigure_dom_object_request_type_instance = ReconfigureDomObjectRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureDomObjectRequestType.to_json()

# convert the object into a dict
reconfigure_dom_object_request_type_dict = reconfigure_dom_object_request_type_instance.to_dict()
# create an instance of ReconfigureDomObjectRequestType from a dict
reconfigure_dom_object_request_type_form_dict = reconfigure_dom_object_request_type.from_dict(reconfigure_dom_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


