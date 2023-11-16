# DVPortgroupRollbackRequestType

The parameters of *DistributedVirtualPortgroup.DVPortgroupRollback_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_backup** | [**EntityBackupConfig**](EntityBackupConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dv_portgroup_rollback_request_type import DVPortgroupRollbackRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupRollbackRequestType from a JSON string
dv_portgroup_rollback_request_type_instance = DVPortgroupRollbackRequestType.from_json(json)
# print the JSON string representation of the object
print DVPortgroupRollbackRequestType.to_json()

# convert the object into a dict
dv_portgroup_rollback_request_type_dict = dv_portgroup_rollback_request_type_instance.to_dict()
# create an instance of DVPortgroupRollbackRequestType from a dict
dv_portgroup_rollback_request_type_form_dict = dv_portgroup_rollback_request_type.from_dict(dv_portgroup_rollback_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


