# UpgradePolicyEnum

The policy setting used to determine when tools are auto-upgraded for a virtual machine  Possible values: - `manual`: No auto-upgrades for tools will be performed for this   virtual machine.      Users must manually invoke the UpgradeTools   operation to update the tools. - `upgradeAtPowerCycle`: When the virtual machine is power-cycled, the system checks   for a newer version of tools when the VM comes back up.      If it   is available, a tools upgrade is automatically performed on the   virtual machine and it is rebooted if necessary.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


