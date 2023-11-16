# StorageVmotionIncompatible

This fault is thrown when Storage DRS tries to migrate disks of a virtual machine to a datastore, but finds that the datastore is incompatible with the given virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.storage_vmotion_incompatible import StorageVmotionIncompatible

# TODO update the JSON string below
json = "{}"
# create an instance of StorageVmotionIncompatible from a JSON string
storage_vmotion_incompatible_instance = StorageVmotionIncompatible.from_json(json)
# print the JSON string representation of the object
print StorageVmotionIncompatible.to_json()

# convert the object into a dict
storage_vmotion_incompatible_dict = storage_vmotion_incompatible_instance.to_dict()
# create an instance of StorageVmotionIncompatible from a dict
storage_vmotion_incompatible_form_dict = storage_vmotion_incompatible.from_dict(storage_vmotion_incompatible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


