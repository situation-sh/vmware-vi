# StorageDrsAutomationConfig

Storage DRS fine grain automation controls  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_load_balance_automation_mode** | **str** | Specifies the behavior of Storage DRS when it generates recommendations for correcting space load imbalance in a datastore cluster.  See *StorageDrsPodConfigInfo*. If specified, this option overrides the datastore cluster level automation behavior defined in the *StorageDrsPodConfigInfo*.  ***Since:*** vSphere API 6.0  | [optional] 
**io_load_balance_automation_mode** | **str** | Specifies the behavior of Storage DRS when it generates recommendations for correcting I/O load imbalance in a datastore cluster.  See *StorageDrsPodConfigInfo*. If specified, this option overrides the datastore cluster level automation behavior defined in the *StorageDrsPodConfigInfo*.  ***Since:*** vSphere API 6.0  | [optional] 
**rule_enforcement_automation_mode** | **str** | Specifies the behavior of Storage DRS when it generates recommendations for correcting affinity rule violations in a datastore cluster.  See *StorageDrsPodConfigInfoBehavior_enum*. If specified, this option overrides the datastore cluster level automation behavior defined in the *StorageDrsPodConfigInfo* for recommendations aimed at fixing rule violations.  ***Since:*** vSphere API 6.0  | [optional] 
**policy_enforcement_automation_mode** | **str** | Specifies the behavior of Storage DRS when it generates recommendations for correcting storage and Vm policy violations in a datastore cluster.  See *StorageDrsPodConfigInfoBehavior_enum*. If specified, this option overrides the datastore cluster level automation behavior defined in the *StorageDrsPodConfigInfo* for recommendations aimed at fixing storage policy violations.  ***Since:*** vSphere API 6.0  | [optional] 
**vm_evacuation_automation_mode** | **str** | Specifies the behavior of Storage DRS when it generates recommendations for datastore evacuations in a datastore cluster.  See *StorageDrsPodConfigInfoBehavior_enum*. If specified, this option overrides the datastore cluster level automation behavior defined in the *StorageDrsPodConfigInfo* for recommendations aimed at evacuating Vms from a datastore.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_automation_config import StorageDrsAutomationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsAutomationConfig from a JSON string
storage_drs_automation_config_instance = StorageDrsAutomationConfig.from_json(json)
# print the JSON string representation of the object
print StorageDrsAutomationConfig.to_json()

# convert the object into a dict
storage_drs_automation_config_dict = storage_drs_automation_config_instance.to_dict()
# create an instance of StorageDrsAutomationConfig from a dict
storage_drs_automation_config_form_dict = storage_drs_automation_config.from_dict(storage_drs_automation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


