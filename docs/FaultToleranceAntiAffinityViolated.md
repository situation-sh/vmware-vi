# FaultToleranceAntiAffinityViolated

More than one VM in the same fault tolerance group are placed on the same host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 4.0  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.fault_tolerance_anti_affinity_violated import FaultToleranceAntiAffinityViolated

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceAntiAffinityViolated from a JSON string
fault_tolerance_anti_affinity_violated_instance = FaultToleranceAntiAffinityViolated.from_json(json)
# print the JSON string representation of the object
print FaultToleranceAntiAffinityViolated.to_json()

# convert the object into a dict
fault_tolerance_anti_affinity_violated_dict = fault_tolerance_anti_affinity_violated_instance.to_dict()
# create an instance of FaultToleranceAntiAffinityViolated from a dict
fault_tolerance_anti_affinity_violated_form_dict = fault_tolerance_anti_affinity_violated.from_dict(fault_tolerance_anti_affinity_violated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


