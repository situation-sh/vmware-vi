# DVSRollbackCapability

The *DVSRollbackCapability* data object describes the rollback capabilities for a *DistributedVirtualSwitch*.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollback_supported** | **bool** | Indicates whether rollback is supported on the distributed switch.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvs_rollback_capability import DVSRollbackCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DVSRollbackCapability from a JSON string
dvs_rollback_capability_instance = DVSRollbackCapability.from_json(json)
# print the JSON string representation of the object
print DVSRollbackCapability.to_json()

# convert the object into a dict
dvs_rollback_capability_dict = dvs_rollback_capability_instance.to_dict()
# create an instance of DVSRollbackCapability from a dict
dvs_rollback_capability_form_dict = dvs_rollback_capability.from_dict(dvs_rollback_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


