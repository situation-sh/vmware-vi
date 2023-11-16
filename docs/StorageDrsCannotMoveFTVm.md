# StorageDrsCannotMoveFTVm

This fault is thrown because Storage DRS cannot generate recommendations to relocate Fault Tolerant VMs across datastores.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_ftvm import StorageDrsCannotMoveFTVm

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveFTVm from a JSON string
storage_drs_cannot_move_ftvm_instance = StorageDrsCannotMoveFTVm.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveFTVm.to_json()

# convert the object into a dict
storage_drs_cannot_move_ftvm_dict = storage_drs_cannot_move_ftvm_instance.to_dict()
# create an instance of StorageDrsCannotMoveFTVm from a dict
storage_drs_cannot_move_ftvm_form_dict = storage_drs_cannot_move_ftvm.from_dict(storage_drs_cannot_move_ftvm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


