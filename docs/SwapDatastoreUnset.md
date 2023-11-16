# SwapDatastoreUnset

The compute resource and/or virtual machine configurations indicate that when executing on the host the virtual machine should use a swap datastore, but the host does not have a swap datastore configured.  If executing on the host the virtual machine would instead use its own directory for swapfile placement. This is a compatibility warning, not an error. Note it is actually the common case for a host to not have a configured swap datastore, and the problem may rest with the compute resource and/or virtual machine configuration; therefore this is not a HostConfigFault.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.swap_datastore_unset import SwapDatastoreUnset

# TODO update the JSON string below
json = "{}"
# create an instance of SwapDatastoreUnset from a JSON string
swap_datastore_unset_instance = SwapDatastoreUnset.from_json(json)
# print the JSON string representation of the object
print SwapDatastoreUnset.to_json()

# convert the object into a dict
swap_datastore_unset_dict = swap_datastore_unset_instance.to_dict()
# create an instance of SwapDatastoreUnset from a dict
swap_datastore_unset_form_dict = swap_datastore_unset.from_dict(swap_datastore_unset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


