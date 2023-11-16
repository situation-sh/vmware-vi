# RectifyDvsHostRequestType

The parameters of *DistributedVirtualSwitch.RectifyDvsHost_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The hosts to be rectified.  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.rectify_dvs_host_request_type import RectifyDvsHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RectifyDvsHostRequestType from a JSON string
rectify_dvs_host_request_type_instance = RectifyDvsHostRequestType.from_json(json)
# print the JSON string representation of the object
print RectifyDvsHostRequestType.to_json()

# convert the object into a dict
rectify_dvs_host_request_type_dict = rectify_dvs_host_request_type_instance.to_dict()
# create an instance of RectifyDvsHostRequestType from a dict
rectify_dvs_host_request_type_form_dict = rectify_dvs_host_request_type.from_dict(rectify_dvs_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


