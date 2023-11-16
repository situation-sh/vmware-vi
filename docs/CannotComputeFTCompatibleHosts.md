# CannotComputeFTCompatibleHosts

This fault is used if FT compatible hosts cannot be computed for a VM  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | Name of the virtual machine  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.cannot_compute_ft_compatible_hosts import CannotComputeFTCompatibleHosts

# TODO update the JSON string below
json = "{}"
# create an instance of CannotComputeFTCompatibleHosts from a JSON string
cannot_compute_ft_compatible_hosts_instance = CannotComputeFTCompatibleHosts.from_json(json)
# print the JSON string representation of the object
print CannotComputeFTCompatibleHosts.to_json()

# convert the object into a dict
cannot_compute_ft_compatible_hosts_dict = cannot_compute_ft_compatible_hosts_instance.to_dict()
# create an instance of CannotComputeFTCompatibleHosts from a dict
cannot_compute_ft_compatible_hosts_form_dict = cannot_compute_ft_compatible_hosts.from_dict(cannot_compute_ft_compatible_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


