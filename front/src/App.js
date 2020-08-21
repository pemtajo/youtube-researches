import React, { Component } from 'react';
import { ThemeProvider } from 'styled-components';
import { Button, themeDefault, Divider, Text } from 'aiq-design-system';
import { Input } from 'reactstrap';
import axios from 'axios'
import YouTube from 'react-youtube';

class Screen extends Component {

  constructor(props) {
    super(props);
    this.state = {
      term: "",
      days: "",
      researchs: ""
    };

  }

  opts = {
    height: '390',
    width: '640',
    playerVars: {
      autoplay: 0,
    },
  };

  doResearch = async () => {
    const days_split = this.state.days.split(',');
    try {
      const r = await axios.post(`http://localhost:12345/researchs`, JSON.stringify({ 'term': this.state.term, 'days': days_split }), { headers: { 'Content-Type': 'application/json' } });
      this.setState({
        researchs: r.data
      });
    } catch (error) {
      alert("Wrong input data");
    }
  }

  changeTerm = (e) => {
    const t = e.target.value;
    this.setState({
      term: t
    });
  }

  changeDays = (e) => {
    const d = e.target.value;
    this.setState({
      days: d
    });
  }

  showTopWords = (words) => {
    let str = "";
    for (var i in words) {
      str += "'" + words[i][0] + "'->" + words[i][1] + "\n ";
    }
    return str;
  }

  showDays = () => {

  }
  render() {
    return (
      <div>
        <Input type="textarea" name="term" placeholder="term" onChange={this.changeTerm} />
        <Input type="textarea" name="days" placeholder="days" onChange={this.changeDays} />
        <Button palette="primary" variant="contained" onClick={this.doResearch} >RESEARCH</Button>
        {
          this.state.researchs &&
          <div>
            <Divider margin={10} height={5} color={'secondary'} />
            <Text>TOP 5 WORD DESCRIPTION: {this.showTopWords(this.state.researchs.words_descriptions)}</Text><br />
            <Text>TOP 5 WORD TITLE: {this.showTopWords(this.state.researchs.words_titles)}</Text><br />
            <Text>WATCH ALL IN  {this.state.researchs.days.length} DAYS</Text><br />
            <ul >
              {this.state.researchs.days.map(day => (
                <div>
                  <Divider width={'100%'} color={'primary'}><Text paddingRight={10} paddingLeft={10}>DAY</Text></Divider>
                  <ul >
                    {day.map(url => (<div><YouTube videoId={url} opts={this.opts} /><br /></div>))}
                  </ul>
                </div>
              ))
              }
            </ul>
          </div>
        }
      </div>
    );
  }
}




function App() {
  return (
    <div className="App">
      <ThemeProvider theme={themeDefault}>
        <Screen />
      </ThemeProvider>
    </div>
  );
}

export default App;
