var player;
var token;

window.onSpotifyWebPlaybackSDKReady = () => {
  token = 'BQC7jlON9nXiGWY5fm1eTvlxXtAMbksqcJ7vskhCXt1-oM__UziIr-mlIHT9710ky6_p0KdyYn_kgy7Qfx8WAwrXzHGz5BCrFO9nWE3NRQpzJhMCYTe-1sz2o-K5WEa71iLrgAIc2Ol2xh1rM6VLUn8yexo2vh3OUn0VqMN8';

  player = new Spotify.Player({
    name: 'Web Playback SDK Quick Start Player',
    getOAuthToken: cb => { cb(token); }
  });

  // Error handling
  player.addListener('initialization_error', ({ message }) => { console.error(message); });
  player.addListener('authentication_error', ({ message }) => { console.error(message); });
  player.addListener('account_error', ({ message }) => { console.error(message); });
  player.addListener('playback_error', ({ message }) => { console.error(message); });

  // Playback status updates
  player.addListener('player_state_changed', state => { console.log(state); });

  // Ready
  player.addListener('ready', ({ device_id }) => {
    console.log('Ready with Device ID', device_id);
  });

  // Not Ready
  player.addListener('not_ready', ({ device_id }) => {
    console.log('Device ID has gone offline', device_id);
  });

  // Connect to the player!
  player.connect();
};

function myFunction(){
  player.getVolume().then(volume => {
    let volume_percentage = volume * 100;
    console.log(`The volume of the player is ${volume}%`);
  });
}

function toggleAudio(){
  console.log('attempting to pause');
  player.togglePlay().then(() => {
    console.log('Toggled playback!');
  });
}

function playAudio(id){

  const play = ({
    spotify_uri,
    playerInstance: {
      _options: {
        getOAuthToken,
        id
      }
    }
  }) => {
    getOAuthToken(access_token => {
      fetch(`https://api.spotify.com/v1/me/player/play?device_id=${id}`, {
        method: 'PUT',
        body: JSON.stringify({ uris: [spotify_uri] }),
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${access_token}`
        },
      });
    });
  };

  play({
    playerInstance: player,
    spotify_uri: 'spotify:track:' + id,
  });
}
