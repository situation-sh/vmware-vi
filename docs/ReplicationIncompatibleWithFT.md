# ReplicationIncompatibleWithFT

Used to indicate that FT cannot be enabled on a replicated virtual machine (returned by *VirtualMachine.QueryFaultToleranceCompatibility*).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.replication_incompatible_with_ft import ReplicationIncompatibleWithFT

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationIncompatibleWithFT from a JSON string
replication_incompatible_with_ft_instance = ReplicationIncompatibleWithFT.from_json(json)
# print the JSON string representation of the object
print ReplicationIncompatibleWithFT.to_json()

# convert the object into a dict
replication_incompatible_with_ft_dict = replication_incompatible_with_ft_instance.to_dict()
# create an instance of ReplicationIncompatibleWithFT from a dict
replication_incompatible_with_ft_form_dict = replication_incompatible_with_ft.from_dict(replication_incompatible_with_ft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


