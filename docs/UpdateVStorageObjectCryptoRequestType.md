# UpdateVStorageObjectCryptoRequestType

The parameters of *VcenterVStorageObjectManager.UpdateVStorageObjectCrypto_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | New profile requirement on the virtual storage object.  ***Since:*** vSphere API 5.5  | [optional] 
**disks_crypto** | [**DiskCryptoSpec**](DiskCryptoSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.update_v_storage_object_crypto_request_type import UpdateVStorageObjectCryptoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVStorageObjectCryptoRequestType from a JSON string
update_v_storage_object_crypto_request_type_instance = UpdateVStorageObjectCryptoRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVStorageObjectCryptoRequestType.to_json()

# convert the object into a dict
update_v_storage_object_crypto_request_type_dict = update_v_storage_object_crypto_request_type_instance.to_dict()
# create an instance of UpdateVStorageObjectCryptoRequestType from a dict
update_v_storage_object_crypto_request_type_form_dict = update_v_storage_object_crypto_request_type.from_dict(update_v_storage_object_crypto_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


