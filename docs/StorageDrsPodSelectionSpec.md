# StorageDrsPodSelectionSpec

Specification for moving or copying a virtual machine to a different Storage Pod.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_vm_config** | [**List[VmPodConfigForPlacement]**](VmPodConfigForPlacement.md) | An optional list that allows specifying the storage pod location for each virtual disk and the VM configurations and overrides to be used during placement.  ***Since:*** vSphere API 5.0  | [optional] 
**storage_pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_pod_selection_spec import StorageDrsPodSelectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsPodSelectionSpec from a JSON string
storage_drs_pod_selection_spec_instance = StorageDrsPodSelectionSpec.from_json(json)
# print the JSON string representation of the object
print StorageDrsPodSelectionSpec.to_json()

# convert the object into a dict
storage_drs_pod_selection_spec_dict = storage_drs_pod_selection_spec_instance.to_dict()
# create an instance of StorageDrsPodSelectionSpec from a dict
storage_drs_pod_selection_spec_form_dict = storage_drs_pod_selection_spec.from_dict(storage_drs_pod_selection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


