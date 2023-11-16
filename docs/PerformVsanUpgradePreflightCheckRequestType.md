# PerformVsanUpgradePreflightCheckRequestType

The parameters of *VsanUpgradeSystem.PerformVsanUpgradePreflightCheck*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**downgrade_format** | **bool** | Intend to perform a on-disk format downgrade instead of upgrade. Adds additional checks.  | [optional] 

## Example

```python
from vmware_vi.models.perform_vsan_upgrade_preflight_check_request_type import PerformVsanUpgradePreflightCheckRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PerformVsanUpgradePreflightCheckRequestType from a JSON string
perform_vsan_upgrade_preflight_check_request_type_instance = PerformVsanUpgradePreflightCheckRequestType.from_json(json)
# print the JSON string representation of the object
print PerformVsanUpgradePreflightCheckRequestType.to_json()

# convert the object into a dict
perform_vsan_upgrade_preflight_check_request_type_dict = perform_vsan_upgrade_preflight_check_request_type_instance.to_dict()
# create an instance of PerformVsanUpgradePreflightCheckRequestType from a dict
perform_vsan_upgrade_preflight_check_request_type_form_dict = perform_vsan_upgrade_preflight_check_request_type.from_dict(perform_vsan_upgrade_preflight_check_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


