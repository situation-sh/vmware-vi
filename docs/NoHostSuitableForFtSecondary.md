# NoHostSuitableForFtSecondary

The NoHostSuitableForFtSecondary fault is thrown when the system is unable to find a suitable host for the Fault Tolerance secondary virtual machine.  This fault can be thrown when Virtual Center is trying to place or power on a Fault Tolerance Secondary, in both DRS or non-DRS cases.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | The name of the primary virtual machine corresponding to the secondary virtual machine.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.no_host_suitable_for_ft_secondary import NoHostSuitableForFtSecondary

# TODO update the JSON string below
json = "{}"
# create an instance of NoHostSuitableForFtSecondary from a JSON string
no_host_suitable_for_ft_secondary_instance = NoHostSuitableForFtSecondary.from_json(json)
# print the JSON string representation of the object
print NoHostSuitableForFtSecondary.to_json()

# convert the object into a dict
no_host_suitable_for_ft_secondary_dict = no_host_suitable_for_ft_secondary_instance.to_dict()
# create an instance of NoHostSuitableForFtSecondary from a dict
no_host_suitable_for_ft_secondary_form_dict = no_host_suitable_for_ft_secondary.from_dict(no_host_suitable_for_ft_secondary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


