# VsanUpgradeSystemPreflightCheckResult

Captures the result of a VSAN upgrade pre-flight check.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issues** | [**List[VsanUpgradeSystemPreflightCheckIssue]**](VsanUpgradeSystemPreflightCheckIssue.md) | Detected issues.  In some cases, not all possible issues are captured, i.e. only the first (few) issues may be captured, and only once those are resolved would additional issues be reported. Absence of issues means the pre-flight check passed.  ***Since:*** vSphere API 6.0  | [optional] 
**disk_mapping_to_restore** | [**VsanHostDiskMapping**](VsanHostDiskMapping.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_preflight_check_result import VsanUpgradeSystemPreflightCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemPreflightCheckResult from a JSON string
vsan_upgrade_system_preflight_check_result_instance = VsanUpgradeSystemPreflightCheckResult.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemPreflightCheckResult.to_json()

# convert the object into a dict
vsan_upgrade_system_preflight_check_result_dict = vsan_upgrade_system_preflight_check_result_instance.to_dict()
# create an instance of VsanUpgradeSystemPreflightCheckResult from a dict
vsan_upgrade_system_preflight_check_result_form_dict = vsan_upgrade_system_preflight_check_result.from_dict(vsan_upgrade_system_preflight_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


