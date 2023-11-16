# PowerOnFtSecondaryFailed

The PowerOnFtSecondaryFailed fault is thrown when the system is unable to power on a Fault Tolerance secondary virtual machine.  It includes a list of failures on different hosts.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | The name of the primary virtual machine corresponding to the secondary that is to be powered on.  ***Since:*** vSphere API 4.0  | 
**host_selection_by** | [**FtIssuesOnHostHostSelectionTypeEnum**](FtIssuesOnHostHostSelectionTypeEnum.md) |  | 
**host_errors** | [**List[MethodFault]**](MethodFault.md) | Information on why the system can not power on a Fault Tolerance secondary virtual machine on specific hosts.  Everything in the array should be FtIssuesOnHost.  ***Since:*** vSphere API 4.0  | [optional] 
**root_cause** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.power_on_ft_secondary_failed import PowerOnFtSecondaryFailed

# TODO update the JSON string below
json = "{}"
# create an instance of PowerOnFtSecondaryFailed from a JSON string
power_on_ft_secondary_failed_instance = PowerOnFtSecondaryFailed.from_json(json)
# print the JSON string representation of the object
print PowerOnFtSecondaryFailed.to_json()

# convert the object into a dict
power_on_ft_secondary_failed_dict = power_on_ft_secondary_failed_instance.to_dict()
# create an instance of PowerOnFtSecondaryFailed from a dict
power_on_ft_secondary_failed_form_dict = power_on_ft_secondary_failed.from_dict(power_on_ft_secondary_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


