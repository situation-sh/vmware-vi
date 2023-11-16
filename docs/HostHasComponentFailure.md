# HostHasComponentFailure

The host has a component failure and thus can cause issues for VMs running or to be running on it.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The host that has the component failure.  ***Since:*** vSphere API 6.0  | 
**component_type** | **str** | The type of the component that has failed.  Values come from *HostHasComponentFailureHostComponentType_enum*.  ***Since:*** vSphere API 6.0  | 
**component_name** | **str** | The name of the component that has failed.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_has_component_failure import HostHasComponentFailure

# TODO update the JSON string below
json = "{}"
# create an instance of HostHasComponentFailure from a JSON string
host_has_component_failure_instance = HostHasComponentFailure.from_json(json)
# print the JSON string representation of the object
print HostHasComponentFailure.to_json()

# convert the object into a dict
host_has_component_failure_dict = host_has_component_failure_instance.to_dict()
# create an instance of HostHasComponentFailure from a dict
host_has_component_failure_form_dict = host_has_component_failure.from_dict(host_has_component_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


