import React, { useState } from "react";
import styled from "styled-components";

const StyledTerminal = styled.div`
  background-color: #f1f1dc;
  color: #6b705c;
  font-family: monospace;
  font-size: 16px;
  padding: 20px;
  width: 100hv;
  height: 100vh;
  display: "flex";
  alignitems: "center";
`;

const StyledPrompt = styled.span`
  color: #a5a58d;
`;

const TerminalContainer = () => {
  const [inputValue, setInputValue] = useState("");
  const [outputValue, setOutputValue] = useState("");

  const onChangeHandler = (event) => {
    setInputValue(event.target.value);
  };

  const onSubmitHandler = async (event) => {
    event.preventDefault();
    const response = await fetch(
      `${process.env.REACT_APP_API_URL}/api/commands/${inputValue}`
    );
    const data = await response.text();
    console.log(data);
    if (response.status === 404) {
      setOutputValue("Command not found");
    } else {
      if (inputValue === "maps") {
        setOutputValue(
          <h3>
            <strong>{data}</strong>
          </h3>
        );
      } else if (inputValue === "help") {
        setOutputValue(
            data
        );
      }
      else {
        setOutputValue("Command not found");
      }

    }
    setInputValue("");
  };

  return (
    <StyledTerminal>
      <div style={{ display: "flex", alignItems: "center", color: "#6b705c" }}>
        <StyledPrompt>
          <h1>$ </h1>
        </StyledPrompt>
        <form onSubmit={onSubmitHandler}>
          <h1>
            <input
              type="text"
              name="name"
              onChange={onChangeHandler}
              value={inputValue}
              style={{
                backgroundColor: "transparent",
                border: "none",
                color: "#6b705c",
                outline: "none",
                width: "100vw",
                fontSize: "inherit",
              }}
              onFocus={(e) => (e.target.style.border = "none")}
            />
          </h1>
        </form>
      </div>
      <div style={{ color: "#c4c4c4" }}>{outputValue}</div>
    </StyledTerminal>
  );
};

export default TerminalContainer;
