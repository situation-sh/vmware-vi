# StorageDrsConfigSpec

The *StorageDrsConfigSpec* data object provides a set of update specifications for storage DRS configuration.  To support incremental changes, these properties are all optional.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_config_spec** | [**StorageDrsPodConfigSpec**](StorageDrsPodConfigSpec.md) |  | [optional] 
**vm_config_spec** | [**List[StorageDrsVmConfigSpec]**](StorageDrsVmConfigSpec.md) | Changes to the per-virtual-machine storage DRS settings.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_config_spec import StorageDrsConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsConfigSpec from a JSON string
storage_drs_config_spec_instance = StorageDrsConfigSpec.from_json(json)
# print the JSON string representation of the object
print StorageDrsConfigSpec.to_json()

# convert the object into a dict
storage_drs_config_spec_dict = storage_drs_config_spec_instance.to_dict()
# create an instance of StorageDrsConfigSpec from a dict
storage_drs_config_spec_form_dict = storage_drs_config_spec.from_dict(storage_drs_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


