# PowerOnFtSecondaryTimedout

PowerOnFtSecondaryTimedout exception is thrown when Virtual Center fails the operation to power on a Fault Tolerance secondary virtual machine because it is taking longer than expected.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | The name of the primary virtual machine corresponding to the secondary that is to be powered on.  ***Since:*** vSphere API 4.0  | 
**timeout** | **int** | The time out value in seconds  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.power_on_ft_secondary_timedout import PowerOnFtSecondaryTimedout

# TODO update the JSON string below
json = "{}"
# create an instance of PowerOnFtSecondaryTimedout from a JSON string
power_on_ft_secondary_timedout_instance = PowerOnFtSecondaryTimedout.from_json(json)
# print the JSON string representation of the object
print PowerOnFtSecondaryTimedout.to_json()

# convert the object into a dict
power_on_ft_secondary_timedout_dict = power_on_ft_secondary_timedout_instance.to_dict()
# create an instance of PowerOnFtSecondaryTimedout from a dict
power_on_ft_secondary_timedout_form_dict = power_on_ft_secondary_timedout.from_dict(power_on_ft_secondary_timedout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


