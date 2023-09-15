// HomeScreen.js
import React from 'react';
import {View, Text, Button, StyleSheet} from 'react-native';
import {NavigationActions} from 'react-navigation';

class HomeScreen extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Text>Welcome to Biogas App</Text>
        <Button
          title="Scan QR Code"
          onPress={() => this.props.navigation.navigate('QRScanner')}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default HomeScreen;
