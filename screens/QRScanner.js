// QRScanner.js
import React, { Component } from 'react';
import { Text, View, StyleSheet } from 'react-native';
import { RNCamera } from 'react-native-camera';

class QRScanner extends Component {
  constructor(props) {
    super(props);
    this.camera = null;
  }

  onBarCodeRead = (e) => {
    // Handle the scanned QR code data here
    console.log('Scanned QR Code:', e.data);
    // You can navigate to the relevant data entry screen or perform other actions
  };

  render() {
    return (
      <View style={styles.container}>
        <RNCamera
          ref={(ref) => {
            this.camera = ref;
          }}
          style={styles.preview}
          onBarCodeRead={this.onBarCodeRead}
          captureAudio={false}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    backgroundColor: 'black',
  },
  preview: {
    flex: 1,
    justifyContent: 'flex-end',
    alignItems: 'center',
  },
});

export default QRScanner;
