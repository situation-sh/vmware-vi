# DVSRollbackRequestType

The parameters of *DistributedVirtualSwitch.DVSRollback_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_backup** | [**EntityBackupConfig**](EntityBackupConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_rollback_request_type import DVSRollbackRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DVSRollbackRequestType from a JSON string
dvs_rollback_request_type_instance = DVSRollbackRequestType.from_json(json)
# print the JSON string representation of the object
print DVSRollbackRequestType.to_json()

# convert the object into a dict
dvs_rollback_request_type_dict = dvs_rollback_request_type_instance.to_dict()
# create an instance of DVSRollbackRequestType from a dict
dvs_rollback_request_type_form_dict = dvs_rollback_request_type.from_dict(dvs_rollback_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


