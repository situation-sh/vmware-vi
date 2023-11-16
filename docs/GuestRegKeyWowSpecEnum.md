# GuestRegKeyWowSpecEnum

This describes the bitness (32-bit or 64-bit) of a registry view in a Windows OS that supports WOW64.  WOW64 (short for Windows 32-bit on Windows 64-bit) is the x86 emulator that allows 32-bit Windows-based applications to run seamlessly on 64-bit Windows. Please refer to these MSDN sites for more details: http://msdn.microsoft.com/en-us/library/aa384249(v=vs.85).aspx and http://msdn.microsoft.com/en-us/library/aa384253(v=vs.85).aspx  Possible values: - `WOWNative`: Access the key from the native view of the   Registry (32-bit on 32-bit versions of Windows,   64-bit on 64-bit versions of Windows). - `WOW32`: Access the key from the 32-bit view of the Registry. - `WOW64`: Access the key from the 64-bit view of the Registry.    ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


