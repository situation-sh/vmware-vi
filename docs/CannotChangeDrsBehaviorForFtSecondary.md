# CannotChangeDrsBehaviorForFtSecondary

This fault is used to report that the DRS behavior cannot be modified for a FT secondary virtual machine  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | Name of the virtual machine  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.cannot_change_drs_behavior_for_ft_secondary import CannotChangeDrsBehaviorForFtSecondary

# TODO update the JSON string below
json = "{}"
# create an instance of CannotChangeDrsBehaviorForFtSecondary from a JSON string
cannot_change_drs_behavior_for_ft_secondary_instance = CannotChangeDrsBehaviorForFtSecondary.from_json(json)
# print the JSON string representation of the object
print CannotChangeDrsBehaviorForFtSecondary.to_json()

# convert the object into a dict
cannot_change_drs_behavior_for_ft_secondary_dict = cannot_change_drs_behavior_for_ft_secondary_instance.to_dict()
# create an instance of CannotChangeDrsBehaviorForFtSecondary from a dict
cannot_change_drs_behavior_for_ft_secondary_form_dict = cannot_change_drs_behavior_for_ft_secondary.from_dict(cannot_change_drs_behavior_for_ft_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


